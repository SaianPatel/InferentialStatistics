%% Basics of Probability - Coin Flip

% Set the random seed
rng(49);

% Set the probability threshold
p = 0.5;

% Set the number of trails
n = 10000;

% Initialise an array with the probabilities over time (H or T, pH)
pT = zeros([n,1]);

pH = [];

% Initialise number of heads
nHeads = 0;
nTails = 0;

% Loop through each trial
for i = 1:n

    p_i = rand(1);

    % If the current probability is below the threshold, it is a Heads
    if p_i <= p

        % Set the 2nd column of pT as 1 to denote Heads
        pT(i,1) = 1;

        % Increment nHeads
        nHeads = nHeads + 1;

        % The current probability of heads is the number of heads currently
        % for the values of i so far
        pH_i = nHeads / i;
        
        % Append to pH
        if i == 1

            pH(i, 1) = pH_i;

        else

            pH(end+1, 1) = pH_i;

        end

    end


end

%% Plotting
figure("Name", 'Coin Flip Probability')
hold on

% Create a flat line at p
pLine = [0, p; nHeads, p];

% Plot the line
plot(pLine(:,1), pLine(:,2), 'Color', 'r', 'LineStyle','--', 'LineWidth',2);

% Plot the probabilities over time
plot((1:nHeads)', pH, 'Color', 'b', 'LineWidth',2);